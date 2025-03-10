class CliCat:
    def __init__(self):
        self.name = "Whiskers"
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.last_interaction = datetime.now()
        self.load_state()
        self.check_time_passed()
        
    def load_state(self):
        """Load pet state from file if it exists"""
        pet_file = os.path.expanduser("~/.clipet")
        if os.path.exists(pet_file):
            try:
                with open(pet_file, 'r') as f:
                    data = json.load(f)
                    self.name = data.get('name', self.name)
                    self.hunger = data.get('hunger', self.hunger)
                    self.happiness = data.get('happiness', self.happiness)
                    self.energy = data.get('energy', self.energy)
                    self.health = data.get('health', self.health)
                    self.last_interaction = datetime.fromisoformat(data.get('last_interaction', datetime.now().isoformat()))
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading pet state: {e}")
    
    def save_state(self):
        """Save pet state to file"""
        pet_file = os.path.expanduser("~/.clipet")
        data = {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy,
            'health': self.health,
            'last_interaction': datetime.now().isoformat()
        }
        with open(pet_file, 'w') as f:
            json.dump(data, f)
    
    def check_time_passed(self):
        """Check time since last interaction and update stats accordingly"""
        now = datetime.now()
        hours_passed = (now - self.last_interaction).total_seconds() / 3600
        
        # Decrease stats based on time passed
        self.hunger = max(0, self.hunger - int(hours_passed * 5))
        self.happiness = max(0, self.happiness - int(hours_passed * 3))
        self.energy = min(100, self.energy + int(hours_passed * 10))
        
        # Health decreases if hunger or happiness is too low
        if self.hunger < 20 or self.happiness < 20:
            self.health = max(0, self.health - int(hours_passed * 2))
            
        self.last_interaction = now
    
    def feed(self):
        """Feed the pet"""
        self.hunger = min(100, self.hunger + 30)
        self.energy = max(0, self.energy - 5)
        if self.hunger > 90:
            print(f"{self.name} is full!")
        else:
            print(f"{self.name} enjoys the meal! Yum!")
        
        # Small chance to get sick from overeating
        if self.hunger > 95 and random.random() < 0.1:
            self.health = max(0, self.health - 10)
            print(f"{self.name} doesn't feel well after eating too much...")
    
    def play(self):
        """Play with the pet"""
        if self.energy < 20:
            print(f"{self.name} is too tired to play right now.")
            return
            
        self.happiness = min(100, self.happiness + 25)
        self.energy = max(0, self.energy - 20)
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} had a great time playing with you!")
        
        # Randomly mimic commands from users bash history
        if random.random() < 0.3:
            self.mimic_bash_command()
    
    def rest(self):
        """Let the pet rest to regain energy"""
        self.energy = min(100, self.energy + 40)
        self.hunger = max(0, self.hunger - 5)
        print(f"{self.name} had a nice nap and feels refreshed!")
    
    def heal(self):
        """Give medicine to improve health"""
        if self.health > 90:
            print(f"{self.name} is already healthy!")
        else:
            self.health = min(100, self.health + 20)
            print(f"{self.name} is feeling better after taking medicine!")
    
    def rename(self, new_name):
        """Rename the pet"""
        old_name = self.name
        self.name = new_name
        print(f"Your pet has been renamed from {old_name} to {self.name}!")
    
    def status(self):
        """Display pet status"""
        return {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness, 
            'energy': self.energy,
            'health': self.health
        }
    
    def get_state_art(self):
        """Return ASCII art based on pet's current state"""
        if self.health < 30:
            return PET_SICK
        if self.hunger < 30:
            return PET_HUNGRY
        if self.energy < 30:
            return PET_SLEEPY
        if self.happiness > 80:
            return PET_PLAYING
        return PET_HAPPY
    
    def mimic_bash_command(self):
        """Read and mimic a random command from bash history"""
        history_file = os.path.expanduser("~/.bash_history")
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r') as f:
                    commands = f.readlines()
                
                # Filter out empty or sensitive commands
                filtered_commands = [cmd.strip() for cmd in commands 
                                    if cmd.strip() and 
                                    not any(s in cmd for s in ['password', 'token', 'key', 'secret'])]
                
                if filtered_commands:
                    command = random.choice(filtered_commands)
                    # Keep it short and simple
                    if len(command) > 30:
                        command = command[:30] + "..."
                    print(f"{self.name} seems to be mimicking you: '{command}' *tilts head*")
            except Exception as e:
                pass  # Silently fail if we can't read bash history
    
    def display(self):
        """Display the pet with its stats"""
        art = self.get_state_art()
        
        # Progress bar for stats
        def stat_bar(value):
            filled = int(value / 10)
            return "[" + "#" * filled + "-" * (10 - filled) + "]"
        
        print("\n" + art)
        print(f"Name: {self.name}")
        print(f"Hunger:    {stat_bar(self.hunger)} {self.hunger}/100")
        print(f"Happiness: {stat_bar(self.happiness)} {self.happiness}/100")
        print(f"Energy:    {stat_bar(self.energy)} {self.energy}/100")
        print(f"Health:    {stat_bar(self.health)} {self.health}/100")
        
        # Status messages
        if self.health < 30:
            print(f"{self.name} doesn't feel well... Please give some medicine!")
        elif self.hunger < 30:
            print(f"{self.name} is hungry! Time for a meal!")
        elif self.energy < 30:
            print(f"{self.name} is tired. Let them rest!")
        elif self.happiness < 30:
            print(f"{self.name} is sad. Play together!")
        else:
            print(f"{self.name} is doing great!")