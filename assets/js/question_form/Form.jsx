import React from 'react';
import ReactDOM from 'react-dom';

import FormComponents from './FormComponents';
/**
 * Factory for creating form components for questions
 */
class Form extends React.Component {

    constructor(props) {
        super(props);
        this.state = {formComponents: new FormComponents()};
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
        this.state.formComponents.push(new FormComponent());
    }

    render() {
        return (
            <div>
                <h1>FormBuilder</h1>
                <input type="button" value="Click Me"></input>
            </div>
        );
    }
}

ReactDOM.render(<Form />, document.getElementById('mount'))
