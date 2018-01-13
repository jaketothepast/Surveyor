import React from 'react';
import ReactDOM from 'react-dom';

/**
 * Factory for creating form components for questions
 */
class Form extends React.Component {
    render() {
        return <h1>FormBuilder</h1>;
    }
}

ReactDOM.render(<Form />, document.getElementById('mount'))
