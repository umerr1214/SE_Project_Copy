# Trajectory Overlay Renderer

This project overlays a trajectory path on a video, along with visual markers for events such as ball bounce, impact, and pitch. The tool uses video processing techniques with OpenCV to visualize the trajectory of a ball in a cricket match. The resulting video will be augmented with decision boxes that show the final outcome of events like the pitch, impact, and wicket.

## Features
- Overlay a trajectory path on a video.
- Mark ball bounce and impact points.
- Display decision boxes for "Pitching", "Impact", "Wickets", and "Final Decision".
- Adjustable slow-down factor for visual effects.
- Supports input via video files and JSON files containing trajectory and ball event data.

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd module-6
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Script Locally (Standalone Mode)

You can test the `TrajectoryOverlayRenderer` class by directly calling it in a Python script or interactive session. To do so, use the following example:

```python
from stream_overlay import TrajectoryOverlayRenderer

renderer = TrajectoryOverlayRenderer(
    video_path="input_video.avi",
    module4_json="module4_output.json",
    module5_json="module5_output.json",
    output_path="output_video.avi",
    slow_factor=3
)
renderer.run()
```


## Output File
An augmented video of type .avi
