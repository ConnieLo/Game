import networkx as nx
import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (width, height).
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Set title of the window
pygame.display.set_caption("Catan Game")


# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 153, 213)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(BLUE)

###################################################
# Initialize an empty graph
G = nx.Graph()

# Add nodes to the graph

i = 0
while i < 54:
    G.add_node(i, type='A')
    i += 1

while i < 19:
    G.add_node(i, type='C')
    i += 1

#G.add_node(1, type='A')
G.add_node(2, type='B')
G.add_node(3, type='C')
#G.add_node(4, type='A')
G.add_node(5, type='B')

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Print the graph information
#print("Number of nodes:", G.number_of_nodes())
#print("Number of edges:", G.number_of_edges())

# Iterate over nodes to get their type
#for node, data in G.nodes(data=True):
#    print(f"Node {node} has type {data['type']}")

################################
# Define the node shapes
node_shapes = {
    'A': 'o',
    'B': '^',
    'C': 's'
}

# Define the node colors
node_colors = {
    'A': (255, 0, 0),
    'B': (0, 255, 0),
    'C': (0, 0, 255)
}

# Draw the nodes
pos = nx.spring_layout(G)
for node, data in G.nodes(data=True):
    x, y = pos[node]
    x = int(x * 300 + 50)
    y = int(y * 300 + 50)
    node_type = data['type']
    node_color = node_colors[node_type]
    node_shape = node_shapes[node_type]
    if node_shape == 'o':
        pygame.draw.circle(screen, node_color, (x, y), 20, 0)
    elif node_shape == '^':
        pygame.draw.polygon(screen, node_color, [(x, y-20), (x-20, y+20), (x+20, y+20)], 0)
    elif node_shape == 's':
        pygame.draw.rect(screen, node_color, (x-20, y-20, 40, 40), 0)

# Draw the edges
for (u, v) in G.edges():
    x1, y1 = pos[u]
    x1 = int(x1 * 300 + 50)
    y1 = int(y1 * 300 + 50)
    x2, y2 = pos[v]
    x2 = int(x2 * 300 + 50)
    y2 = int(y2 * 300 + 50)
    pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)


# Define button properties
button_width = 100
button_height = 50
button_x = (screen_width - button_width) / 2
button_y = (screen_height - button_height) / 2

# Load font to display on the button
font = pygame.font.Font(None, 36)

############################################

# Loop until the user clicks the close button.
done = False

pygame.display.update()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the user clicked on the button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                done = True


    # Render the "Exit" text on the button
    text = font.render("Exit", True, BLACK)
    screen.blit(text, (button_x + button_width / 2 - text.get_width() / 2,
                       button_y + button_height / 2 - text.get_height() / 2))

    # Draw the button
    pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height), 1)


    # Limit to 60 frames per second
    clock.tick(60)

    # Update the screen with what we've drawn.
    pygame.display.flip()

# Close the window and quit.
pygame.quit()