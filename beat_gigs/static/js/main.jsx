var Gig = React.createClass({
    render: function () {
        var aspectRatio = this.props.width / this.props.height;
        var WIDTH = 400;
        var height = WIDTH * (1.0 / aspectRatio) - 1;
        var style = {
            width: WIDTH,
            height: height,
            backgroundSize: `${WIDTH}px`
        };
        if (this.props.image_url) {
            style.backgroundImage = 'url(' + this.props.image_url + ')';
        }
        return (
            <div className="gig" style={style}>
                <h2>{this.props.name}</h2>
                {/*<div className="venue">{this.props.venue}</div>*/}
                {/*<p>{this.props.price}</p>*/}
            </div>
        );
    }
});

var loadGigImage = function(gig) {
    var img = new Image();
	var p = new Promise(function(resolve, reject) {
        img.onload = function () {
            gig.img = img;
            resolve(gig);
        };
        img.onerror = function() {
            reject(img);
        };
        img.src = gig.image_url;
    });
	return p;
};


var Gigs = React.createClass({

    getInitialState: function() {
        return {
            gigs: null,
            imagesLoaded: false
        }
    },

    componentDidMount: function() {
        var gigs = [];

        var imagePromises = [];
        for (var gig of this.props.gigs) {
            var image_url = gig.image_url !== null ? gig.image_url.trim() : null;
            if (image_url) {
                imagePromises.push(loadGigImage(gig));
            }
            //gigs.push(<Gig {...gig} width={img.width} height={img.height}/>)
            //gigs.push(<Gig {...gig} />)
        }

        Promise.all(imagePromises).then((gigs) => {
            this.setState({
                imagesLoaded: true,
                gigs: gigs
            });
        });
    },

    render: function () {
        if (this.state.imagesLoaded === true) {
            var NUM_COLUMNS = 3;
            var gigs = [];
            for (var gig of this.state.gigs) {
                gigs.push(<Gig {...gig} width={gig.img.width} height={gig.img.height} />);
            }
            var columns = [];
            for (var i = 0; i < NUM_COLUMNS; i++) {
                columns[i] = [];
            }

            for (var i = 0; i < this.state.gigs.length; i++) {
                var gig = this.state.gigs[i];
                columns[i % 3].push(<Gig {...gig} width={gig.img.width} height={gig.img.height} />);
            }
            var columnsHtml = [];

            for (var column of columns) {
                columnsHtml.push(<div className="col">{column}</div>);
            }
            return (
                <div className="gigs">
                    {columnsHtml}
                </div>
            );
        } else {
            return <div>loading...</div>;
        }
    }
});

var GigGuide = React.createClass({

    getInitialState: function() {
        return {
            date: this.props.date,
            gigData: null
        }
    },

    componentDidMount: function() {
        this.loadDate(today);
    },

    loadDate: function(date) {
        this.setState({
            gigData: null,
            date: date
        });
        var dateStr = date.format('YYYY-MM-DD');
        $.get(`/api/gigs/${dateStr}/`).done(
          (gigData) => {
              this.setState({
                  gigData: gigData
              });
          }
        );
    },

    next: function(e) {
        e.preventDefault();
        var nextDate = this.state.date.clone().add(1, 'days');
        this.loadDate(nextDate);
    },

    prev: function(e) {
        e.preventDefault();
        var nextDate = this.state.date.clone().subtract(1, 'days');
        this.loadDate(nextDate);
    },

    render: function () {

        var isToday = this.state.date.isSame(moment(), "day");
        var isTomorrow = this.state.date.isSame(moment().add(1, 'day'), "day");
        var prettyDate = this.state.date.format('dddd');
        if (isToday) {
            prettyDate = 'Today';
        }
        if (isTomorrow) {
            prettyDate = `Tomorrow (${prettyDate})`;
        }
        if (this.state.gigData !== null) {
            var gigs = <Gigs gigs={this.state.gigData} />
        } else {
            var gigs = <p>loading...</p>;
        }
        return (
            <div className="wrapper">
                <h3 className="menu">
                    <a className="btn prev" href="" onClick={this.prev}>prev</a>
                    {prettyDate}
                    <a className="btn next" href="" onClick={this.next}>next</a>
                </h3>
                {gigs}
            </div>
        );
    }
});


var today = moment();
React.render(
    <GigGuide date={today}/>,
    document.getElementById('app')
);

