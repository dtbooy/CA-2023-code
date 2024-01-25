import { closeConnection, EntryModel, CategoryModel } from "./db.js";

const categories = [
  {
    name: "Food",
    entries: [{ content: "Pizza is ok" }, { content: "I liek chocolate milk" }],
  },
  { name: "Gaming", entries: [{ content: "It's all objects" }] },
  {
    name: "Coding",
    entries: [{ content: "I think I might be able to code something oneday" }],
  },
  {
    name: "Other",
    entries: [
      {
        content:
          "10 things you need to know about rocket rollerblades. I'm going to make this entry reallly really long",
      },
      { content: "Are you a Ninja?" },
    ],
  },
];

//delete all documents in entry model
await CategoryModel.deleteMany();
console.log("Deleted Categories");

await CategoryModel.insertMany(categories);
console.log("Inserted Categories");

// const entries = [
//   { category: "Food", content: "Pizza is ok" },
//   { category: "Food", content: "I liek chocolate milk" },
//   { category: "Gaming", content: "It's all objects" },
//   {
//     category: "Coding",
//     content: "I think I might be able to code something oneday",
//   },
//   {
//     category: "Other",
//     content:
//       "10 things you need to know about rocket rollerblades. I'm going to make this entry reallly really long",
//   },
//   { category: "Other", content: "Are you a Ninja?" },
// ];

//delete all documents in entry model
await EntryModel.deleteMany();
console.log("Deleted Entries");

// await EntryModel.insertMany(entries);
// console.log("Inserted Entries");

closeConnection();
