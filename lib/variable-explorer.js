'use babel';

import { CompositeDisposable } from "atom";
import React from "react";
import ReactTable from "react-table";

// This component is in charge of getting state into the React system.
export default class VariableExplorer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tableData: [],
    };
    this.subscriptions = null;
  }

  handleUpdateVars(data) {
    this.setState(prevState => ({
      tableData: data
    }));
  }

  componentDidMount() {
    this.subscriptions = new CompositeDisposable();
    this.subscriptions.add(
      this.props.emitter.on('did-update-vars', this.handleUpdateVars.bind(this)),
    );
  }

  componentWillUnmount() {
    if (this.subscriptions) {
      this.subscriptions.dispose();
      this.subscriptions = null;
    }
  }

  render() {
    return (
      <VariableExplorerRenderer data={this.state} />
    );
  }
}

class VariableExplorerRenderer extends React.Component {
  render() {
    return (
      <div class="hpy-variable-explorer">
        <ReactTable
          data={this.props.data.tableData}
          columns={[
            {
              Header: "Name",
              accessor: "name",
            },
            {
              Header: "Type",
              accessor: "type",
              maxWidth: 75,
            },
            {
              Header: "Size",
              accessor: "size",
              maxWidth: 75,
              // accessor: d => d.size
            },
            {
              Header: "Value",
              accessor: "value",
            },
          ]}
          defaultPageSize={100}
          showPageSizeOptions={false}
          minRows={20}
          className="-striped -highlight hpy-variable-table"
          noDataText="Variable explorer will initialize once you run a chunk of code. This experimental feature was tested with Python 3 only."
        />
      </div>
    );
  }
}
