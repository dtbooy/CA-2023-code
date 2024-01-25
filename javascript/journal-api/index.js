// move categories to routes
// complete categories CRUD
// Add route: /categories/:cat_id/ - return all entries in category


import express from "express";
import { CategoryModel } from "./db.js";
import entryRoutes from "./routes/entry_routes.js"
// Register app
const app = express();

// This parses the body of the request into json and saves it in req.body
app.use(express.json());

// Attach Entry Router Middleware
app.use("/entries", entryRoutes)

// status 200 is automatic so not required but you can change it like this
app.get("/", (req, res) => {
  res.status.send({ location: "Home" });
});

app.get("/categories", async (req, res) => {
  res.status(200).send(await CategoryModel.find());
});

// start up app
app.listen(4002);
