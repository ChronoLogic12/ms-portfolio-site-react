function Slide(props) {
	return (
		<div className="embla__slide">
			<img src={props.slide.background_image} />
			<h3>{props.slide.title}</h3>
			<h3>{props.slide.description}</h3>
			<a href={props.slide.live_site_url} target="_blank">
				Live site
			</a>
			<a href={props.slide.git_repository_url} target="_blank">
				GitHub Repository
			</a>
		</div>
	);
}

export default Slide;
