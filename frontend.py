"""
Reflex Frontend
React-like UI components written in pure Python
"""
import reflex as rx
import httpx


class State(rx.State):
    """The app state."""
    result: str = ""
    name: str = ""
    loading: bool = False
    
    async def fetch_hello(self):
        """Fetch hello message from API"""
        self.loading = True
        self.result = "Loading..."
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://127.0.0.1:8000/api/hello")
                data = response.json()
                self.result = f"Message: {data['message']}\nStatus: {data['status']}"
        except Exception as e:
            self.result = f"Error: {str(e)}"
        finally:
            self.loading = False
    
    async def fetch_greeting(self):
        """Fetch personalized greeting from API"""
        if not self.name:
            self.result = "Please enter a name"
            return
        
        self.loading = True
        self.result = "Loading..."
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://127.0.0.1:8000/api/greet/{self.name}")
                data = response.json()
                self.result = f"Message: {data['message']}\nName: {data['name']}\nStatus: {data['status']}"
        except Exception as e:
            self.result = f"Error: {str(e)}"
        finally:
            self.loading = False
    
    async def fetch_items(self):
        """Fetch items list from API"""
        self.loading = True
        self.result = "Loading..."
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://127.0.0.1:8000/api/items")
                data = response.json()
                items_text = "\n".join([f"• {item['name']}: {item['description']}" 
                                       for item in data['items']])
                self.result = f"Items:\n{items_text}"
        except Exception as e:
            self.result = f"Error: {str(e)}"
        finally:
            self.loading = False


def index() -> rx.Component:
    """The main page."""
    return rx.container(
        rx.vstack(
            rx.heading("FastAPI + Reflex Web Application", size="9"),
            rx.text(
                "Welcome to your FastAPI backend with Reflex frontend!",
                size="5",
            ),
            
            rx.heading("Test API Endpoints", size="7", margin_top="2em"),
            
            # Hello button
            rx.button(
                "Get Hello Message",
                on_click=State.fetch_hello,
                size="3",
                color_scheme="green",
                margin_top="1em",
            ),
            
            # Name input and greeting button
            rx.hstack(
                rx.input(
                    placeholder="Enter your name",
                    value=State.name,
                    on_change=State.set_name,
                    size="3",
                    width="300px",
                ),
                rx.button(
                    "Get Personalized Greeting",
                    on_click=State.fetch_greeting,
                    size="3",
                    color_scheme="blue",
                ),
                margin_top="1em",
                spacing="3",
            ),
            
            # Items button
            rx.button(
                "Get Items List",
                on_click=State.fetch_items,
                size="3",
                color_scheme="purple",
                margin_top="1em",
            ),
            
            # Result display
            rx.box(
                rx.text(
                    State.result,
                    white_space="pre-wrap",
                    font_family="monospace",
                ),
                background_color=rx.color("gray", 3),
                padding="1em",
                border_radius="8px",
                min_height="100px",
                margin_top="2em",
                width="100%",
            ),
            
            spacing="4",
            align="center",
        ),
        max_width="800px",
        padding="2em",
    )


# Create the app
app = rx.App()
app.add_page(index)
