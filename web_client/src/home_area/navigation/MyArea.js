import React, { Component } from 'react';
import '../styles/my_area.css'
import axios from "axios"

class MyArea extends Component {

    //remplacer les données de this.state par le fetch "get" sur le back-end, puis remplir les champs 'status', 'msg' et 'data' avec la réponse JSON de la requête
    //Crée une fonction pour le faire et faire une setState pour attribuer les nouvelles données de la requete


    constructor(props)
    {
        super(props);
        this.state = {
            status: '200',
            msg: 'Get user services success !',
            data: []
        };
        this.renderCurrentArea = this.renderCurrentArea.bind(this);
    }

    componentDidMount() {
        var uuid = localStorage.getItem('uuid');
        console.log("uuid: " + uuid);
        axios.get("http://localhost:8080/get_user_areas/", {params: {uuid: uuid}}).then(
            (response) => {
                console.log(response.data);
                this.setState(response.data)
            }
        ).catch(function (err) {
            alert(err)
        });
    }

    renderCurrentArea(title)
    {
        const { data } = this.state;
        var currField = title == "Services" ? "service" : (title == "Actions" ? "action" : "reaction");
        const renderCurrentField = field => (
            <li id="list-item-area" key={field[currField]}>
                { field[currField] }
            </li>
        );
        const divStyle = {
            color: '#0065A6',
            weight: 'bold',
            margin: 30
        };

        return (
            <div id="current-area">
                <h2 style={divStyle}>
                    {title} :
                    <div id="bottom-line-area"></div>
                </h2>
                <ul className="list-group-area">
                    { data.map(renderCurrentField) }
                </ul>
            </div>
        )
    }

    deleteAreas() {
        var uuid = localStorage.getItem('uuid');
        axios.post("http://localhost:8080/delete_user_areas/", {uuid: uuid}).then(
            function (response) {
                alert(response.data.msg)
            }
        ).catch(function (err) {
            alert(err)
        })
    }

    render()
    {
        const fieldTitle = ["Services", "Actions", "Reactions"];
        const renderCurrentArea = title => this.renderCurrentArea(title);

        return (
            <div id="my-area" style={{textAlign: "center"}}>
                <h1 id="header-area">
                    My AREA
                </h1>
                <br/>
                <button id="button-area" onClick={this.deleteAreas}>Delete my AREA</button>
                <br/>
                { fieldTitle.map(renderCurrentArea) }
            </div>
        );
    }
}

export default MyArea;
