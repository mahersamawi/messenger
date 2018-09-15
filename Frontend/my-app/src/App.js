import React, { Component } from 'react';
import './App.css';
import io from 'socket.io-client';
import { Container, Col } from 'reactstrap';

var ip = "192.168.1.2";
var socket = io('http://' + ip + ':5000');

class App extends Component {
  constructor(){
    super();
    this.state = {
      room: "",
      text: "",
      old_messages : []
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.makeList = this.makeList.bind(this);
    this.addToList = this.addToList.bind(this);
  }


  addToList(msg){
    console.log("Before state");
    console.log(this.state.old_messages);
    if (Array.isArray(this.state.old_messages) === true){
      var arr = this.state.old_messages;
      arr.push(msg);
      console.log("Settng state");
      this.setState({old_messages: arr});
    }
  }


  makeList(list){
    console.log(Array.isArray(list));
    if (Array.isArray(list) === true){
      var listItems = list.map((list) =>
        <li>{list}</li>
      );
      return (
        <ul>{listItems}</ul>
      );
    }
  }


  componentDidMount(){
    socket.on('connect', function() {
    var send_dict = {};
      send_dict['msg'] = "User has connected!";
      send_dict['room'] = "None";
      send_dict['time'] = Date.now();
      socket.send(send_dict);
    });
    // just for testing 
    var test = this;
    socket.emit("join", 'poop'); 
    socket.on('message', function(msg) {
      console.log('Received message');
      console.log(msg);
      console.log(test);
      test.addToList(msg);
    });
    let url = "http://192.168.1.2:5000/room_messages";
    

    return fetch(url)
      .then((response) => 
        response.json()
        .then((responseJson) => {
          console.log(responseJson.messsages);
          this.setState({ old_messages: responseJson.messsages })
        })
        .catch((error) => {
          console.log(error);
          })
        )
  }
    
  handleSubmit(event){
    console.log("send it");
    event.preventDefault();
    var send_dict = {};
    send_dict['msg'] = this.state.text;
    send_dict['room'] = "poop";
    send_dict['time'] = Date.now();
    socket.send(send_dict);
    this.setState(
    {
      text: ""
    });
  }

  handleChange(event) {
    console.log("here");
    this.setState(
    {
        text: event.target.value
    });
  }

  render() {
    return (
      <Container className="top">
        <Col className="Rooms">
          <p> room </p>
        </Col>
        <Col className="Text">
          <h1> text </h1>
          <ul>{this.makeList(this.state.old_messages)}</ul>,
          <form onSubmit={this.handleSubmit}>
          <label>
            <input type="text" value={this.state.text} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
        </Col>
        <Col className="Members">
          <p> members </p>
        </Col>
      </Container>
    );
  }
}

export default App;
