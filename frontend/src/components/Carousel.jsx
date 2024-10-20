import { useEffect } from "react";
import useEmblaCarousel from "embla-carousel-react";

import Slide from "./Slide";

function Carousel(props) {
	const [emblaRef, emblaApi] = useEmblaCarousel({ loop: false });

	useEffect(() => {
		if (emblaApi) {
			console.log(emblaApi.slideNodes());
		}
	}, [emblaApi]);

	return (
		<div className="embla" ref={emblaRef}>
			<div className="embla__container">
				{props.slides.map((slide) => (
					<Slide slide={slide} key={slide.title} />
				))}
			</div>
		</div>
	);
}

export default Carousel;
