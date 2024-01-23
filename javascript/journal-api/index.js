import express from "express";
import mongoose from "mongoose"


const categories = ["Food", "Gaming", "Coding", "Other"];

const entries = [
  { category: "Food", content: "Pizza is ok" },
  { category: "Food", content: "I liek chocolate milk" },
  { category: "Gaming", content: "It's all objects" },
  {
    category: "Coding",
    content: "I think I might be able to code something oneday",
  },
  {
    category: "Other",
    content:
      "10 things you need to know about rocket rollerblades. I'm going to make this entry reallly really long",
  },
  { category: "Other", content: "Are you a Ninja?" },
];

//URI Saved in .env
const uri = DB_URI;
//connect mongoose - should be done as early as possible (before register app)
mongoose.connect(uri)
  .then(m=> console.log(m.connection.readyState === 1 ? "MongoDB Connected." : "MongoDB failed to connect"))
  .catch(err=>console.log(err));

// Create schema - schemas are plural
const entriesSchema = new mongoose.Schema({
  category: {type: String, required: true},
  content: {type: String, required: true}
})
// Create Model - model is singular
const EntryModel = mongoose.model('Entry', entriesSchema)

// Register app
const app = express();

// This parses the body of the request into json and saves it in req.body
app.use(express.json());

// status 200 is automatic so not required but you can change it like this
app.get("/", (req, res) => {
  res.status.send({ location: "Home" });
});

app.get("/categories", (req, res) => {
  res.status(200).send(categories);
});

app.get("/entries", (req, res) => {
  res.status(200).send(entries);
});

/// ":" prefix indicates id is a restful parameter
app.get("/entries/:id", (req, res) => {
  const entry = entries[req.params.id - 1];
  if (entry) {
    res.send(entry);
  } else {
    res.status(404).send({ error: "Entry not found" });
  }
});

app.post("/entries", async (req, res) => {
  // Get data from request
  // console.log(req.body);
  // TO DO: validate
  //Create new entry object
  // const newEntry = req.body;
  // push entry to array!
  // entries.push(newEntry);
  try {
  const insertedEntry = await EntryModel.create(req.body)
  // res with 201, newEntry
  res.status(201).send(insertedEntry);
  }
  catch (err) {
    res.status(400).send({error: err.message});
  }
});

// start up app
app.listen(4001);
