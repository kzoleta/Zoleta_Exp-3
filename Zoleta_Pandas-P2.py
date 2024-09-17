{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "92a28aec-7c07-43f5-9547-cd78672f3b76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n",
      "\n",
      "Row with Model 'Mazda RX4':\n",
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n",
      "\n",
      "The 'Camaro Z28' has 8 cylinders.\n",
      "\n",
      "Cylinders and Gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':\n",
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "#Input validation for loading the CSV file\n",
    "try:\n",
    "    url = \"http://bit.ly/Cars_file\"\n",
    "    cars = pd.read_csv(url)\n",
    "\n",
    "    if cars.empty:\n",
    "        raise ValueError(\"The CSV file is loaded, but it is empty.\")\n",
    "    \n",
    "    #Display the first five rows with odd-numbered columns\n",
    "    print(cars.iloc[:5, ::2])  # :5 for first 5 rows, ::2 to skip columns\n",
    "\n",
    "    #Display the row with Mazda RX4\n",
    "    mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']\n",
    "    if mazda_rx4.empty:\n",
    "        print(\"No car with model 'Mazda RX4' found.\")\n",
    "    else:\n",
    "        print(\"\\nRow with Model 'Mazda RX4':\")\n",
    "        print(mazda_rx4)\n",
    "    \n",
    "    #Camaro Z28 cylinders\n",
    "    camaro_z28 = cars[cars['Model'] == 'Camaro Z28']\n",
    "    if camaro_z28.empty:\n",
    "        print(\"No car with model 'Camaro Z28' found.\")\n",
    "    else:\n",
    "        cyl_camaro = camaro_z28['cyl'].values[0]\n",
    "        print(f\"\\nThe 'Camaro Z28' has {cyl_camaro} cylinders.\")\n",
    "    \n",
    "    #Determine cylinders and gear type for selected models\n",
    "    selected_models = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]\n",
    "    if selected_models.empty:\n",
    "        print(\"No cars found for the selected models.\")\n",
    "    else:\n",
    "        print(\"\\nCylinders and Gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':\")\n",
    "        print(selected_models[['Model', 'cyl', 'gear']])\n",
    "\n",
    "except pd.errors.ParserError as e:\n",
    "    print(\"Error parsing the CSV file:\", e)\n",
    "except FileNotFoundError:\n",
    "    print(\"The CSV file could not be found.\")\n",
    "except Exception as e:\n",
    "    print(\"An error occurred:\", e)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
