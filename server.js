const express = require("express");
const app = express();
const cors = require("cors");

app.use(cors());

app.use(express.json());

let str = {
  st: "",
};

app.post("/api", (req, res) => {
  const string = req.body;
  str.st = string.st;
  console.log(str.st);
  res.send("success");
});

app.get("/api", (req, res) => {
 
  res.send(str.st);
  str.st = "";
});

// Modify the listen function to specify the IP address
app.listen(5000, '192.168.11.104', () => {
  console.log("Server running on http://192.168.11.104:5000");
});
