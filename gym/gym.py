class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        output = ''
        needed_subscription = list(filter(lambda x: x.id == subscription.id, self.subscriptions))
        needed_customer = list(filter(lambda x: x.id == customer.id, self.customers))
        needed_trainer = list(filter(lambda x: x.id == trainer.id, self.trainers))
        needed_equipment = list(filter(lambda x: x.id == equipment.id, self.equipment))
        needed_plan = list(filter(lambda x: x.id == plan.id, self.plans))
        output += Subscription.__repr__(needed_subscription[0]) + '\n'
        output += Customer.__repr__(needed_customer[0]) + '\n'
        output += Trainer.__repr__(needed_trainer[0]) + '\n'
        output += Equipment.__repr__(needed_equipment[0]) + '\n'
        output += ExercisePlan.__repr__(needed_plan[0])
        return output


