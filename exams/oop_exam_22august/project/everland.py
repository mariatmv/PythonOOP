from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost

        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            if room.expenses + room.room_cost > room.budget:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                output.append(f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= room.expenses + room.room_cost

        return '\n'.join(output)

    def status(self):
        output = [f'Total population: {sum([x.members_count for x in self.rooms])}']
        for room in self.rooms:
            output.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.__class__.__name__ == 'YoungCoupleWithChildren':
                n = 1
                for child in room.children:
                    output.append(f"--- Child {n} monthly cost: {(child.cost * 30):.2f}$")
                    n += 1

            appliances_for_month = sum([x.get_monthly_expense() for x in room.appliances])
            output.append(f"--- Appliances monthly cost: {appliances_for_month:.2f}$")

        return "\n".join(output)