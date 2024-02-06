// import React from "react";
import Home from "./Home";
import CategorySelection from "./CategorySelection";
import NewEntry from "./NewEntry";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavBar from "./NavBar";
import { useState } from "react";

const App = () => {
  const [categories, setCategories] = useState([
    "Food",
    "Gaming",
    "Code",
    "Other",
  ]);

  const [ entries, setEntries] = useState([])

  function addEntry(catId, entry) {
    // 1. Create newEntry Object
    const newEntry = {
      category: catId,
      content: entry
    }
  
  // 2. Store it somewhere? (temp step as we aren't connecting to the API yet) 
  setEntries([...entries, newEntry])
  }

  return (
    <>
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home categories={categories} entries={entries}/>} />
          <Route
            path="/category"
            element={<CategorySelection categories={categories} />}
          />
          <Route path="/entry">
            <Route
              path="new/:cat_id"
              element={<NewEntry addEntry={addEntry} categories={categories} />}
            />
          </Route>
          <Route path="*" element={<h3> 404: Page not found </h3>} />
        </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
