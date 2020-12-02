-- trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.

CREATE TRIGGER decr BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
set quantity = quantity - NEW.number
where name = NEW.item_name;
