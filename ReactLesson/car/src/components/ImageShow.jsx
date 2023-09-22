
export const ImageShow = ({image}) => {
    return (
        <div>
            <img  src={image.urls.small} alt={image.all_description}/>
        </div>
      )
};