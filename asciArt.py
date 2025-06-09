import time
import random
import os
import math

class GalaxySimulator:
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        self.stars = []
        self.spiral_arms = []
        self.center_x = width // 2
        self.center_y = height // 2
        self.time_step = 0
        
        # Generate spiral galaxy structure
        self.generate_spiral_galaxy()
        
    def generate_spiral_galaxy(self):
        # Create spiral arms
        for arm in range(3):  # 3 spiral arms
            arm_offset = (2 * math.pi * arm) / 3
            for r in range(5, min(self.width//2, self.height//2) - 2):
                # Spiral equation: theta = a * r + offset
                theta = 0.3 * r + arm_offset + random.uniform(-0.2, 0.2)
                
                x = self.center_x + int(r * math.cos(theta))
                y = self.center_y + int(r * math.sin(theta) * 0.5)  # Flatten vertically
                
                if 0 <= x < self.width and 0 <= y < self.height:
                    # Add some randomness to make it look more natural
                    if random.random() < 0.7:  # 70% chance for star in spiral arm
                        brightness = random.choice(['*', '·', '•', '◦', '○'])
                        self.stars.append({
                            'x': x, 'y': y, 'brightness': brightness,
                            'twinkle_phase': random.uniform(0, 2*math.pi),
                            'twinkle_speed': random.uniform(0.1, 0.3)
                        })
        
        # Add random field stars
        for _ in range(50):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            brightness = random.choice(['·', '◦', '*'])
            self.stars.append({
                'x': x, 'y': y, 'brightness': brightness,
                'twinkle_phase': random.uniform(0, 2*math.pi),
                'twinkle_speed': random.uniform(0.05, 0.2)
            })
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def render_frame(self):
        # Create empty canvas
        canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw galaxy center (black hole)
        if 0 <= self.center_y < self.height and 0 <= self.center_x < self.width:
            canvas[self.center_y][self.center_x] = '●'
        
        # Draw twinkling stars
        for star in self.stars:
            x, y = star['x'], star['y']
            if 0 <= x < self.width and 0 <= y < self.height:
                # Calculate twinkle effect
                twinkle = math.sin(star['twinkle_phase'] + self.time_step * star['twinkle_speed'])
                if twinkle > 0.3:  # Star is bright enough to show
                    canvas[y][x] = star['brightness']
        
        # Convert canvas to string and display
        frame = '\n'.join(''.join(row) for row in canvas)
        
        # Add some cosmic info
        info = f"🌌 GALAXY SIMULATOR 🌌\nTime: {self.time_step:.1f} | Stars: {len(self.stars)} | Press Ctrl+C to exit"
        
        self.clear_screen()
        print(info)
        print("─" * self.width)
        print(frame)
        print("─" * self.width)
    
    def animate(self, duration=30):
        """Run the galaxy animation for specified duration"""
        start_time = time.time()
        
        try:
            while time.time() - start_time < duration:
                self.render_frame()
                time.sleep(0.1)
                self.time_step += 0.1
                
                # Occasionally add a shooting star
                if random.random() < 0.02:
                    self.add_shooting_star()
                    
        except KeyboardInterrupt:
            print("\n\n🌟 Thanks for exploring the galaxy! 🌟")
    
    def add_shooting_star(self):
        """Add a temporary shooting star effect"""
        start_x = random.randint(0, self.width-1)
        start_y = random.randint(0, self.height-1)
        
        # Create trail
        for i in range(5):
            x = start_x + i
            y = start_y
            if 0 <= x < self.width and 0 <= y < self.height:
                trail_star = {
                    'x': x, 'y': y, 'brightness': '✦',
                    'twinkle_phase': 0, 'twinkle_speed': 0.5
                }
                self.stars.append(trail_star)
        
        # Remove shooting star after a moment
        def remove_trail():
            time.sleep(1)
            for _ in range(5):
                if self.stars:
                    self.stars.pop()
        
        import threading
        threading.Thread(target=remove_trail, daemon=True).start()

def main():
    # Create and run galaxy simulation
    print("🚀 Initializing Galaxy Simulator...")
    time.sleep(1)
    
    galaxy = GalaxySimulator(width=70, height=20)
    galaxy.animate(duration=60)  # Run for 60 seconds

if __name__ == "__main__":
    main()