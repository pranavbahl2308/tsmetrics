from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


major = 0
minor = 1
patch = 0
version = '.'.join([str(v) for v in [major, minor, patch]])


setup(name='tsmetrics',
      version=version,
      description='Evaluation metrics for time series analysis',
      url='https://github.com/pranavbahl2308/tsmetrics',
      download_url='https://github.com/pranavbahl2308/tsmetrics',

      long_description=readme(),
      author='Pranav Bahl',
      author_email='pranavshekharbahl@gmail.com',
      license='MIT',
      keywords=['python', 'timeseries', 'evaluation', 'metrics', 'rmse', 'mse',
                'mae', 'mape', 'mase', 'smape', 'sse', 'smse', 'nmse'],

      packages=['tsmetrics'],
      install_requires=[
          'numpy'
      ],
      include_package_data=True,

      zip_safe=False)
