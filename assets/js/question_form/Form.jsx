import React from 'react';
import ReactDOM from 'react-dom';

import FormComponents from './FormComponents';
import FormComponent from './FormComponent';

/**
 * Factory for creating form components for questions
 */
class Form extends React.Component {

    constructor(props) {
        super(props);
        this.state = {formComponents: []};

        this.newFormComponent = this.newFormComponent.bind(this);
    }

    /* Lifecycle hooks */

    /* Runs after component output rendered to DOM */
    componentDidMount() {

    }

    /* Runs after removed from DOM */
    componentWillUnmount() {

    }

    /* Need a call to this.setState for button pushes */

    newFormComponent() {
        this.state.formComponents.push({message: "im a component"})
        // TODO -- have a form component chooser widget that provides input to add component
        // TODO -- each child in array should have unique "KEY" prop
        ReactDOM.render(<Form />, document.getElementById('mount'))
    }

    render() {
        return (
            <div>
                <h1>FormBuilder</h1>
                <input type="button" value="Click Me" onClick={this.newFormComponent}></input>
                <div id="formComponentContainer" >
                    <FormComponents componentList={this.state.formComponents} />
                </div>
            </div>
        );
    }
}

ReactDOM.render(<Form />, document.getElementById('mount'))
