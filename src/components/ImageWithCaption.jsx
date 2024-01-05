import React from "react";

export const ImageWithCaption = ({ src, caption, source }) => {
  return (
    <figure>
      <img src={src} alt={caption} />
      <figcaption>
        {caption} {source && <a href={source}>Zdroj</a>}
      </figcaption>
    </figure>
  );
};
