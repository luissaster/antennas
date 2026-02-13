# Antennas

### Interactive Geovisualization for ANATEL's MOSAICO Data

A Django application to visualize antenna data from [ANATEL's MOSAICO system](https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php) on an interactive map.

## Features

-   **CSV Upload**: Easily upload antenna data exports (CSV) from the MOSAICO system.
-   **Data Processing**: Automatic data cleaning and validation using Pandas.
-   **Interactive Map**: Visualize antenna locations markers.
-   **Filtering**: Filter displayed antennas by **Technology** and **Entity**.
-   **Clustering**: Groups antennas at the same coordinates to improve map readability.

## Installation

### Prerequisites

-   Python 3.8+
-   Django
-   Pandas

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/luissaster/antennas.git
    cd antennas
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

5.  Access the application at `http://127.0.0.1:8000/`.

## Usage

1.  Navigate to the **Upload** page.
2.  Select a CSV file containing the antenna data.
3.  Once uploaded, you will be redirected to the **Map** view.
4.  Use the filters to refine the visualization by technology or entity.

## Docker Support

You can also run the project using Docker:

```bash
docker-compose up --build
```
