from robocorp.tasks import task
from RPA.JavaAccessBridge import JavaAccessBridge
import subprocess

@task
def automate_java():

    try:
        # Initialize the Java Access Bridge
        jab = JavaAccessBridge()

        # Open the targeted Java Application
        command = ["java", "-jar", "BasicSwing.jar", "Chat Frame"]
        process = subprocess.Popen( command, cwd=".", close_fds=True )

        # Select the Java Application
        jab.select_window_by_title("Chat Frame")

        # Use different locators to identify & arguments to identify particular elements
        # Use different actions to manipulate those elements
        jab.type_text(
            "role:text",
            "text for the textarea",
            enter=True
        )
        jab.type_text(
            "role:text",
            "text for the input field",
            index=1,
            clear=True
        )

        jab.click_element("role:push button and name:Send")

    except Exception as e:
        # If there's any error, you can handle it here
        print(f"An error occurred: {e}")
        raise e

    finally:
        # Teardown the Java application
        process.terminate()
        # Wait for the process to actually terminate
        process.wait(timeout=2)
