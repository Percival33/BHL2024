import {Card} from "./Card";
import {useState} from "react";

export function Gallery(props) {
    const [cards, setCards] = useState(props.cards);
    // const card = cards[0];
    // console.log(card);
    return (
      <div className="flex flex-wrap justify-center w-full gap-4">
        {cards.map((card) => (
          <div className="w-1/2 md:w-1/3 lg:w-1/4 p-2" key={card.key}>
            <Card {...card} />
          </div>
        ))}
      </div>
    );
}
