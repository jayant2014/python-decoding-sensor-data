class HouseInfo:
    HouseInfo(self, data):
        seld.data = data

    def get_data_by_area(self, field, rec_area = 0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(date):
        field_data = []
        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])
        return field_data 
