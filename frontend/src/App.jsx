import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

import Portfolio from "./Pages/Portfolio";
import Header from "./components/Header";

function App() {
	return (
		<>
			<Header />
			<Portfolio />
		</>
	);
}

export default App;
