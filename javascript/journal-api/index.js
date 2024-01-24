import express from "express";
import { EntryModel, CategoryModel } from "./db.js";

const categories = ["Food", "Gaming", "Coding", "Other"];

// Register app
const app = express();

// This parses the body of the request into json and saves it in req.body
app.use(express.json());

// status 200 is automatic so not required but you can change it like this
app.get("/", (req, res) => {
  res.status.send({ location: "Home" });
});

app.get("/categories", async (req, res) => {
  res.status(200).send(await CategoryModel.find());
});

app.get("/entries", async (req, res) => {
  res.status(200).send(await EntryModel.find());
});

/// ":" prefix indicates id is a restful parameter
app.get("/entries/:id", async (req, res) => {
  const entry = await EntryModel.findById(req.params.id);
  if (entry) {
    res.send(entry);
  } else {
    res.status(404).send({ error: "Entry not found" });
  }
});

// PostRequest
app.post("/entries", async (req, res) => {
  try {
    const insertedEntry = await EntryModel.create(req.body);
    // res with 201, newEntry
    res.status(201).send(insertedEntry);
  } catch (err) {
    res.status(500).send({ error: err.message });
  }
});

// Put Request
app.put("/entries/:id", async (req, res) => {
  try {
    // findByIdAndUpdate
    const updatedEntry = await EntryModel.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    // res with 200 (default - .status not required), newEntry
    if (updatedEntry) {
      res.send(updatedEntry);
    } else {
      res.status(404).send({ error: "Entry not found" });
    }
  } catch (err) {
    res.status(500).send({ error: err.message });
  }
});


// DELETE Request
app.delete("/entries/:id", async (req, res) => {
  try {
    // findByIdAndUpdate
    const updatedEntry = await EntryModel.findByIdAndDelete(
      req.params.id,
      req.body
    );
    // res with 200 (default - .status not required), newEntry
    if (updatedEntry) {
      res.sendStatus(204);
    } else {
      res.status(404).send({ error: "Entry not found" });
    }
  } catch (err) {
    res.status(500).send({ error: err.message });
  }
});

// start up app
app.listen(4002);
