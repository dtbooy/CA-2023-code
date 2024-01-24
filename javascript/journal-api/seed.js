import { closeConnection, EntryModel } from "./db.js"

const entries = [
  { category: "Food", content: "Pizza is ok" },
  { category: "Food", content: "I liek chocolate milk" },
  { category: "Gaming", content: "It's all objects" },
  { category: "Coding", content: "I think I might be able to code something oneday"},
  { category: "Other", content: "10 things you need to know about rocket rollerblades. I'm going to make this entry reallly really long"},
  { category: "Other", content: "Are you a Ninja?" },
];

//delete all documents in entry model
await EntryModel.deleteMany()
console.log("Deleted Entries")

await EntryModel.insertMany(entries)
console.log("Inserted Entries")

closeConnection()