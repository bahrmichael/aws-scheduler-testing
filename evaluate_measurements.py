import matplotlib.pyplot as plt
from model import MeasuredDuration


def download():
    delays = []
    counter = 0
    for item in MeasuredDuration.scan():
        delays.append(item.delay)
        counter += 1
        if counter % 1000 == 0:
            print(f'{counter}')
    return delays


if __name__ == '__main__':
    data = download()

    print(f'total: {len(data)}')
    plt.hist(data, bins=100)

    plt.title(f'Regular Scaled ({len(data)} events)')
    plt.xlabel("Delay after scheduled time (milliseconds)")
    plt.ylabel("Number of events")
    plt.savefig('regular.png')

    plt.yscale('log')
    plt.xscale('log')
    plt.title(f'Log Scaled ({len(data)} events)')
    plt.xlabel("Delay after scheduled time (milliseconds)")
    plt.ylabel("Number of events")
    plt.savefig('log.png')

    print('Diagrams saved to regular.png and log.png')
