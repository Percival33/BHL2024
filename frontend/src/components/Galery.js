import { Card } from "./Card";

export function Gallery() {
  const [cards, setCards] = useState([]);
  return (
    <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
      {cards.map((card) => (
        <Card title={card.title} description={card.description} />
      ))}
    </div>
  );
}
