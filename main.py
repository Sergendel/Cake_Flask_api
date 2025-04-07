from extract.extract_file import ExtractFile
from transform.transform_processing import TransformProcessing
from transform.transform_model import TransformModel
import config


def main():

    # extract data
    extract = ExtractFile(config.FILE_PATH)
    dataset = extract.load_data()

    # transform
    transform = TransformProcessing(config)
    dataset_transform = transform.transform(dataset)
    #print(dataset_transform)

    # predict
    model = TransformModel(config)
    result = model.predict(dataset_transform)
    print(result)


if __name__ == "__main__":
    main()