import React from "react";

export const Navigation = ({ links }) => {
  return (
    <nav style={{ position: "sticky", top: "1rem", justifyContent: "end", padding: "0 1rem" }}>
      <ul>
        <li role="list" dir="rtl">
          <details role="list">
            <summary aria-haspopup="listbox" role="button">
              Jít na kapitolu
            </summary>
            <ul role="listbox">
              {links.map((item) => (
                <li key={item.id}>
                  <a href={item.id}>{item.label}</a>
                </li>
              ))}
            </ul>
          </details>
        </li>
      </ul>
    </nav>
  );
};
