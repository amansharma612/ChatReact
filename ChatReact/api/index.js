const express = require("express");
const app = express()
const axios = require("axios").default
const cors = require("cors")
const port = 8080
app.use(cors())
app.use(express.json())
app.post('/res', (req, res) => {
    let msgToSend = "";
    console.log(req.body.message)
    axios.post('http://127.0.0.1:8888/message/', {message:req.body.message}, {
        headers: {
            'content-type':'application/json'
        }
    })
    .then((response)=> {
        msgToSend = response.data.message
        console.log(msgToSend)
        res.json({message: msgToSend})
        res.end()
    })
    .catch((err) => {
        console.log(err)
        
    })
    
})


app.listen(port, () =>{
    console.log(`Chat AI server listening on ${port}`)
})

