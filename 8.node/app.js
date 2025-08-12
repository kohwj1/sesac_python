const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.send('hello world from node.js')
})

app.listen(3000, () => {
    console.log('server is ready!')
})