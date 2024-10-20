import React, { useEffect, useState } from "react";
import axios from "axios";

import Carousel from "../components/Carousel";

function Portfolio() {
	const [slides, setSlides] = useState([{"title": "tile 1"}]);

	useEffect(() => {
		axios
			.get("http://localhost:8000/api/portfolio/")
			.then((response) => {
				console.log(response.data);
				setSlides(response.data);
			})
			.catch((error) => {
				console.error("Error fetching data", error);
			});
	}, []);

	return (
		<>
			<Carousel slides={slides} />
		</>
	);
}

export default Portfolio;
