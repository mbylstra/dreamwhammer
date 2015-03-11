var DjangoSettings = React.createClass({

    componentDidMount: function() {
        console.log('did mount!');
        $.get('/django-docs/api/settings/').done(
            (settings) => {
                this.setState({
                    settings: settings
                });
            }
        );
    },

    getInitialState: function() {
        return {
            settings: [],
            search: ''
        }
    },

    onSearchChange: function(e) {
        this.setState({
            search: e.target.value
        });
    },

    render: function() {
        var settings = [];
        for (var setting of this.state.settings) {
            var name = setting.variable.replace('¶', '').toLowerCase();
            //console.log('name', name);
            var query = this.state.search.toLowerCase();
            if (query === '' || name.search(query) >= 0) {
                settings.push(
                    <tr>
                        <th>{setting.variable.replace('¶', '')}</th>
                        <td>{setting.default}</td>
                    </tr>
                );
            }
        }
        return (
            <div>
                <h1>Django settings lookup</h1>
                <input onChange={this.onSearchChange} />
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Default</th>
                        </tr>
                    </thead>
                    {settings}
                </table>
            </div>
        );
    }
});

React.render(
    <DjangoSettings />,
    document.getElementById('app')
);

