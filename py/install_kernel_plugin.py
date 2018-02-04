from IPython.display import display, JSON

def install_kernel_plugin():
    numeric_types = [int, float]
    try:
        # TODO(nikita): base python2 handling on reported python version
        numeric_types.append(long)
    except:
        pass
    numeric_types = tuple(numeric_types)

    # TODO(nikita): test if 'numpy' in sys.modules, to avoid introducing numpy
    # import when the kernel doesn't need it
    try:
        import numpy as np
        def isarray(obj):
            return isinstance(obj, np.ndarray)
        isscalar = np.isscalar
    except:
        def isarray(obj):
            return False
        def isscalar(obj):
            return False

    class HydrogenPythonPlugin:
        def __init__(self):
            self.shell = get_ipython()

        def report(self, val):
            display(JSON({'hydrogen_python': val}))

        def run(self, method, *args, **kwargs):
            try:
                getattr(self, method)(*args, **kwargs)
            except Exception as e:
                self.report({
                    'error': str(e),
                })

        def variable_explorer_hook(self):
            # This code based on the source of the %whos IPython magic
            user_ns = self.shell.user_ns
            user_ns_hidden = self.shell.user_ns_hidden
            names = [name for name in user_ns
                if not name.startswith('_') and not (
                    (name in user_ns_hidden)
                    and (user_ns[name] is user_ns_hidden[name]))]

            kb = 1024
            Mb = 1048576 # kb**2

            manifest = []
            for name in names:
                val = user_ns[name]

                entry_size = ''
                entry_type = type(val).__name__
                entry_value = ''

                if isinstance(val, numeric_types):
                    entry_value = val
                elif isinstance(val, complex):
                    entry_value = str(val).lstrip('(').rstrip(')')
                elif isinstance(val, (list, set, dict, tuple)):
                    entry_size = len(val)
                elif isinstance(val, str):
                    entry_size = len(val)
                    if entry_size < 20:
                        entry_value = val
                    else:
                        entry_value = val[:10] + "..." + val[-10:]
                elif isarray(val):
                    entry_size = str(val.shape).replace(',','').replace(' ','x')[1:-1]
                    entry_type = str(val.dtype)
                    try:
                        vbytes = val.size * val.itemsize
                        entry_value = "Bytes: {}".format(str(vbytes))
                        if vbytes < 100000:
                            pass
                        elif vbytes < Mb:
                            entry_value += " ({} kb)".format(vbytes/kb)
                        else:
                            entry_value += " ({} Mb)".format(vbytes/Mb)
                    except:
                        pass
                elif isscalar(val):
                    entry_value = str(val)

                manifest.append({
                    'name': name,
                    'size': entry_size,
                    'type': entry_type,
                    'value': entry_value,
                    })
            self.report({'variables': manifest})

    get_ipython()._hydrogen_python = HydrogenPythonPlugin()

    return {
        'success': True
    }

try:
    result = install_kernel_plugin()
    display(JSON({'hydrogen_python': result}))
except:
    display(JSON({'hydrogen_python': {'success': False}}))
