import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config();

//URI Saved in .env
//connect mongoose - should be done as early as possible (before register app)
mongoose
  .connect(process.env.DB_URI)
  .then((m) =>
    console.log(
      m.connection.readyState === 1
        ? "MongoDB Connected."
        : "MongoDB failed to connect"
    )
  )
  .catch((err) => console.log(err));

// close db on SIGnal TERMination
process.on("SIGTERM", () => {
    mongoose.disconnect()
    console.log("MongoDB disconnect")
});

// Create schema - schemas are plural
const entriesSchema = new mongoose.Schema({
  category: { type: String, required: true },
  content: { type: String, required: true },
});
// Create Model - model is singular
const EntryModel = mongoose.model("Entry", entriesSchema);

export { EntryModel };