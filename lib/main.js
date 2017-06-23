'use babel';

import { CompositeDisposable, Disposable } from 'atom';

const HydrogenPythonPlugin = {
  subscriptions: null,
  hydrogen: null,

  activate() {
    this.subscriptions = new CompositeDisposable();
  },

  deactivate() {
    this.subscriptions.dispose();
  },

  consumeHydrogen(hydrogen) {
    this.hydrogen = hydrogen;

    this.hydrogen.onDidCreateKernel((kernel) => {
      if (!kernel || kernel.language != 'python') {
        return;
      }

      let executeActive = false;
      kernel.onWillExecute(event => {
        if (executeActive || !event.callWatches) {
          return;
        }

        event.cancel();
        executeActive = true;
        const newCode = "print('Plugin injection!')\n" + event.code;
        kernel.execute(newCode, event.callWatches, event.onResults);
        executeActive = false;
      });
    })


    return new Disposable(() => {
      this.hydrogen = null;
    });
  },
};

export default HydrogenPythonPlugin;
