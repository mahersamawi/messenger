import React, { Component } from 'react';
import './App.css';
import io from 'socket.io-client';
import { Container, Row, Col } from 'reactstrap';

var ip = "192.168.1.2";
var socket = io('http://' + ip + ':5000');


class App extends Component {
  constructor(){
    super();
    this.state = {
      room: "",
      text: ""
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  componentDidMount(){
      socket.on('connect', function() {
      var send_dict = {};
      send_dict['msg'] = "User has connected!";
      send_dict['room'] = "None";
      socket.send(send_dict);
    });
  }

  handleSubmit(event){
    console.log("send it");
    event.preventDefault();
    var send_dict = {};
    send_dict['msg'] = this.state.text;
    send_dict['room'] = this.state.room;
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
          <p> text </p>
        </Col>
        <Col className="Members">
          <p> members </p>
        </Col>
      </Container>
    );
  }
}

export default App;
