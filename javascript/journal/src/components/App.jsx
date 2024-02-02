import React from "react";
import Home from "./Home";
import CategorySelection from "./CategorySelection";
import NewEntry from "./NewEntry";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";

const App = () => {
  return (
    <>
      <h1 className="title">Journal</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/category" element={<CategorySelection />} />
          <Route path="/entry">
            <Route path="new" element={<NewEntry />} />
          </Route>
          <Route path="*" element={ <h3> 404: Page not found </h3> } />
        </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
