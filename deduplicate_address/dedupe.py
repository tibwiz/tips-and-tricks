import csv


class Dedupe:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        data = []
        with open(self.input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                m_street = row['Primary Contact: Mailing Street']
                if m_street is None or m_street == '':
                    continue
                m_city = row['Primary Contact: Mailing City']
                if m_city is None or m_city == '':
                    print(f'City is empty for {m_street}')
                    continue
                m_state = row['Primary Contact: Mailing State/Province']
                m_zip = row['Primary Contact: Mailing Zip/Postal Code']
                m_country = row['Primary Contact: Mailing Country']
                # print(f'Street:{m_street}, City: {m_city}, State: {m_state}, Zip: {m_zip}, Country: {m_country}')
                if m_city in m_street:
                    m_street = m_street.split(m_city)[0]
                data.append({
                    'Street': m_street,
                    'City': m_city,
                    'State': m_state,
                    'Country': m_country,
                    'Zip': m_zip})

        fieldnames = ['Street', 'City', 'State', 'Zip', 'Country']
        with open(self.output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    dedupe = Dedupe('address.csv', 'output.csv')
    dedupe.run()
