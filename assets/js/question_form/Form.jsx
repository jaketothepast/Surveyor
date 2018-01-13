import React from 'react';
import ReactDOM from 'react-dom';

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
            <h1>FormBuilder</h1>
            <input type="button">Create Form Component</input>
            <FormComponents />
        );
    }
}

ReactDOM.render(<Form />, document.getElementById('mount'))
https://angel.co/
