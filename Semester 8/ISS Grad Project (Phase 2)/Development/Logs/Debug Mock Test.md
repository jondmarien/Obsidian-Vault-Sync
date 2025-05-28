---
title: Debug Mock Test
author:
  - Jon Marien
created: 2025-05-22
published: 2025-05-22
tags:
  - capstone
---

| Title           | Author                       | Created      | Published    | Tags                     |
| --------------- | ---------------------------- | ------------ | ------------ | ------------------------ |
| Debug Mock Test | <ul><li>Jon Marien</li></ul> | May 22, 2025 | May 22, 2025 | [[#capstone\|#capstone]] |

```sh

[2025-05-22T00:02:11.514099] Packet received (Total: 10): b'TEST-9'
2025-05-22 00:02:16,515 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-10'
2025-05-22 00:02:16,516 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 16, 516162, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:16.516355] Packet received (Total: 11): b'TEST-10'
2025-05-22 00:02:21,517 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-11'
2025-05-22 00:02:21,517 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 21, 517224, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:21.517329] Packet received (Total: 12): b'TEST-11'
2025-05-22 00:02:26,518 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-12'
2025-05-22 00:02:26,518 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 26, 518501, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:26.518597] Packet received (Total: 13): b'TEST-12'
2025-05-22 00:02:31,519 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-13'
2025-05-22 00:02:31,519 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 31, 519747, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:31.519858] Packet received (Total: 14): b'TEST-13'
2025-05-22 00:02:36,520 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-14'
2025-05-22 00:02:36,521 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 36, 521025, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:36.521130] Packet received (Total: 15): b'TEST-14'
2025-05-22 00:02:41,522 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-15'
2025-05-22 00:02:41,522 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 41, 522739, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:41.522863] Packet received (Total: 16): b'TEST-15'
2025-05-22 00:02:46,523 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-16'
2025-05-22 00:02:46,523 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 46, 523631, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:46.523743] Packet received (Total: 17): b'TEST-16'
2025-05-22 00:02:51,525 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-17'
2025-05-22 00:02:51,525 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 51, 525499, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:51.525714] Packet received (Total: 18): b'TEST-17'
2025-05-22 00:02:56,526 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-18'
2025-05-22 00:02:56,526 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 2, 56, 526392, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:02:56.526495] Packet received (Total: 19): b'TEST-18'
2025-05-22 00:03:01,527 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-19'
2025-05-22 00:03:01,527 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 1, 527698, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:01.527799] Packet received (Total: 20): b'TEST-19'
2025-05-22 00:03:06,528 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-20'
2025-05-22 00:03:06,528 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 6, 528898, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:06.529138] Packet received (Total: 21): b'TEST-20'
2025-05-22 00:03:11,529 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-21'
2025-05-22 00:03:11,530 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 11, 530044, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:11.530139] Packet received (Total: 22): b'TEST-21'
2025-05-22 00:03:16,530 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-22'
2025-05-22 00:03:16,530 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 16, 530533, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:16.530645] Packet received (Total: 23): b'TEST-22'
2025-05-22 00:03:21,531 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-23'
2025-05-22 00:03:21,531 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 21, 531584, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:21.531880] Packet received (Total: 24): b'TEST-23'
2025-05-22 00:03:26,533 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-24'
2025-05-22 00:03:26,534 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 26, 534044, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:26.534176] Packet received (Total: 25): b'TEST-24'
2025-05-22 00:03:31,535 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-25'
2025-05-22 00:03:31,535 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 31, 535969, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:31.536076] Packet received (Total: 26): b'TEST-25'
2025-05-22 00:03:36,536 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-26'
2025-05-22 00:03:36,536 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 36, 536524, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:36.536657] Packet received (Total: 27): b'TEST-26'
2025-05-22 00:03:41,538 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-27'
2025-05-22 00:03:41,538 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 41, 538782, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:41.538885] Packet received (Total: 28): b'TEST-27'
2025-05-22 00:03:46,539 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-28'
2025-05-22 00:03:46,540 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 46, 540078, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:46.540177] Packet received (Total: 29): b'TEST-28'
2025-05-22 00:03:51,542 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-29'
2025-05-22 00:03:51,542 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 51, 542424, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:51.542640] Packet received (Total: 30): b'TEST-29'
2025-05-22 00:03:56,543 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-30'
2025-05-22 00:03:56,543 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 3, 56, 543415, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:03:56.543592] Packet received (Total: 31): b'TEST-30'
2025-05-22 00:04:01,545 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-31'
2025-05-22 00:04:01,545 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 1, 545237, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:01.545329] Packet received (Total: 32): b'TEST-31'
2025-05-22 00:04:06,547 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-32'
2025-05-22 00:04:06,547 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 6, 547366, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:06.547549] Packet received (Total: 33): b'TEST-32'
2025-05-22 00:04:11,547 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-33'
2025-05-22 00:04:11,547 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 11, 547975, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:11.548153] Packet received (Total: 34): b'TEST-33'
2025-05-22 00:04:16,548 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-34'
2025-05-22 00:04:16,548 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 16, 548969, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:16.549063] Packet received (Total: 35): b'TEST-34'
2025-05-22 00:04:21,549 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-35'
2025-05-22 00:04:21,550 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 21, 550425, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:21.550701] Packet received (Total: 36): b'TEST-35'
2025-05-22 00:04:26,552 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-36'
2025-05-22 00:04:26,552 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 26, 552589, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:26.552685] Packet received (Total: 37): b'TEST-36'
2025-05-22 00:04:31,553 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-37'
2025-05-22 00:04:31,553 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 31, 553939, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:31.554043] Packet received (Total: 38): b'TEST-37'
2025-05-22 00:04:36,554 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-38'
2025-05-22 00:04:36,554 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 36, 554545, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:36.554674] Packet received (Total: 39): b'TEST-38'
2025-05-22 00:04:41,555 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-39'
2025-05-22 00:04:41,555 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 41, 555596, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:41.555868] Packet received (Total: 40): b'TEST-39'
2025-05-22 00:04:46,557 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-40'
2025-05-22 00:04:46,557 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 46, 557339, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:46.557435] Packet received (Total: 41): b'TEST-40'
2025-05-22 00:04:51,558 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-41'
2025-05-22 00:04:51,558 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 51, 558820, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:51.558933] Packet received (Total: 42): b'TEST-41'
2025-05-22 00:04:56,561 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-42'
2025-05-22 00:04:56,561 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 4, 56, 561256, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:04:56.561392] Packet received (Total: 43): b'TEST-42'
2025-05-22 00:05:01,562 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-43'
2025-05-22 00:05:01,562 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 1, 562907, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:01.563029] Packet received (Total: 44): b'TEST-43'
2025-05-22 00:05:06,564 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-44'
2025-05-22 00:05:06,565 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 6, 565079, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:06.565182] Packet received (Total: 45): b'TEST-44'
2025-05-22 00:05:11,565 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-45'
2025-05-22 00:05:11,565 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 11, 565791, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:11.565976] Packet received (Total: 46): b'TEST-45'
2025-05-22 00:05:16,566 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-46'
2025-05-22 00:05:16,566 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 16, 566952, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:16.567076] Packet received (Total: 47): b'TEST-46'
2025-05-22 00:05:21,567 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-47'
2025-05-22 00:05:21,567 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 21, 567647, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:21.567749] Packet received (Total: 48): b'TEST-47'
2025-05-22 00:05:26,569 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-48'
2025-05-22 00:05:26,570 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 26, 570131, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:26.570283] Packet received (Total: 49): b'TEST-48'
2025-05-22 00:05:31,572 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-49'
2025-05-22 00:05:31,572 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 31, 572513, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:31.572638] Packet received (Total: 50): b'TEST-49'
2025-05-22 00:05:36,572 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-50'
2025-05-22 00:05:36,573 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 36, 573074, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:36.573168] Packet received (Total: 51): b'TEST-50'
2025-05-22 00:05:41,575 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-51'
2025-05-22 00:05:41,575 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 41, 575409, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:41.575641] Packet received (Total: 52): b'TEST-51'
2025-05-22 00:05:46,577 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-52'
2025-05-22 00:05:46,577 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 46, 577605, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:46.577709] Packet received (Total: 53): b'TEST-52'
2025-05-22 00:05:51,578 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-53'
2025-05-22 00:05:51,578 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 51, 578897, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:51.578991] Packet received (Total: 54): b'TEST-53'
2025-05-22 00:05:56,580 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-54'
2025-05-22 00:05:56,580 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 5, 56, 580521, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:05:56.580723] Packet received (Total: 55): b'TEST-54'
2025-05-22 00:06:01,581 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-55'
2025-05-22 00:06:01,581 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 1, 581683, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:01.581780] Packet received (Total: 56): b'TEST-55'
2025-05-22 00:06:06,582 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-56'
2025-05-22 00:06:06,582 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 6, 582675, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:06.582773] Packet received (Total: 57): b'TEST-56'
2025-05-22 00:06:11,585 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-57'
2025-05-22 00:06:11,585 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 11, 585385, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:11.585661] Packet received (Total: 58): b'TEST-57'
2025-05-22 00:06:16,586 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-58'
2025-05-22 00:06:16,587 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 16, 587072, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:16.587318] Packet received (Total: 59): b'TEST-58'
2025-05-22 00:06:21,588 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-59'
2025-05-22 00:06:21,588 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 21, 588279, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:21.588387] Packet received (Total: 60): b'TEST-59'
2025-05-22 00:06:26,589 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-60'
2025-05-22 00:06:26,589 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 26, 589396, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:26.589499] Packet received (Total: 61): b'TEST-60'
2025-05-22 00:06:31,590 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-61'
2025-05-22 00:06:31,591 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 31, 591084, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:31.591339] Packet received (Total: 62): b'TEST-61'
2025-05-22 00:06:36,592 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-62'
2025-05-22 00:06:36,592 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 36, 592389, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:36.592503] Packet received (Total: 63): b'TEST-62'
2025-05-22 00:06:41,594 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-63'
2025-05-22 00:06:41,594 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 41, 594200, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:41.594303] Packet received (Total: 64): b'TEST-63'
2025-05-22 00:06:46,595 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-64'
2025-05-22 00:06:46,595 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 46, 595773, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:46.596077] Packet received (Total: 65): b'TEST-64'
2025-05-22 00:06:51,597 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-65'
2025-05-22 00:06:51,597 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 51, 597297, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:51.597402] Packet received (Total: 66): b'TEST-65'
2025-05-22 00:06:56,597 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-66'
2025-05-22 00:06:56,597 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 6, 56, 597739, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:06:56.597854] Packet received (Total: 67): b'TEST-66'
2025-05-22 00:07:01,598 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-67'
2025-05-22 00:07:01,599 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 1, 599104, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:01.599332] Packet received (Total: 68): b'TEST-67'
2025-05-22 00:07:06,600 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-68'
2025-05-22 00:07:06,600 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 6, 600404, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:06.600499] Packet received (Total: 69): b'TEST-68'
2025-05-22 00:07:11,601 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-69'
2025-05-22 00:07:11,601 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 11, 601327, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:11.601437] Packet received (Total: 70): b'TEST-69'
2025-05-22 00:07:16,602 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-70'
2025-05-22 00:07:16,603 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 16, 603080, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:16.603333] Packet received (Total: 71): b'TEST-70'
2025-05-22 00:07:21,604 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-71'
2025-05-22 00:07:21,604 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 21, 604592, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:21.604717] Packet received (Total: 72): b'TEST-71'
2025-05-22 00:07:26,605 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-72'
2025-05-22 00:07:26,605 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 26, 605518, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:26.605618] Packet received (Total: 73): b'TEST-72'
2025-05-22 00:07:31,606 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-73'
2025-05-22 00:07:31,607 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 31, 607165, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:31.607407] Packet received (Total: 74): b'TEST-73'
2025-05-22 00:07:36,609 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-74'
2025-05-22 00:07:36,609 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 36, 609420, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:36.609532] Packet received (Total: 75): b'TEST-74'
2025-05-22 00:07:41,610 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-75'
2025-05-22 00:07:41,610 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 41, 610396, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:41.610491] Packet received (Total: 76): b'TEST-75'
2025-05-22 00:07:46,611 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-76'
2025-05-22 00:07:46,611 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 46, 611641, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:46.611778] Packet received (Total: 77): b'TEST-76'
2025-05-22 00:07:51,613 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-77'
2025-05-22 00:07:51,613 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 51, 613314, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:51.613482] Packet received (Total: 78): b'TEST-77'
2025-05-22 00:07:56,614 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-78'
2025-05-22 00:07:56,614 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 7, 56, 614767, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:07:56.614874] Packet received (Total: 79): b'TEST-78'
2025-05-22 00:08:01,615 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-79'
2025-05-22 00:08:01,615 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 1, 615652, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:01.615774] Packet received (Total: 80): b'TEST-79'
2025-05-22 00:08:06,616 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-80'
2025-05-22 00:08:06,616 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 6, 616503, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:06.616685] Packet received (Total: 81): b'TEST-80'
2025-05-22 00:08:11,618 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-81'
2025-05-22 00:08:11,618 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 11, 618197, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:11.618299] Packet received (Total: 82): b'TEST-81'
2025-05-22 00:08:16,619 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-82'
2025-05-22 00:08:16,619 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 16, 619122, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:16.619220] Packet received (Total: 83): b'TEST-82'
2025-05-22 00:08:21,620 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-83'
2025-05-22 00:08:21,620 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 21, 620737, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:21.620856] Packet received (Total: 84): b'TEST-83'
2025-05-22 00:08:26,621 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-84'
2025-05-22 00:08:26,621 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 26, 621972, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:26.622084] Packet received (Total: 85): b'TEST-84'
2025-05-22 00:08:31,623 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-85'
2025-05-22 00:08:31,623 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 31, 623728, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:31.623835] Packet received (Total: 86): b'TEST-85'
2025-05-22 00:08:36,624 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-86'
2025-05-22 00:08:36,624 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 36, 624816, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:36.625052] Packet received (Total: 87): b'TEST-86'
2025-05-22 00:08:41,626 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-87'
2025-05-22 00:08:41,626 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 41, 626520, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:41.626621] Packet received (Total: 88): b'TEST-87'
2025-05-22 00:08:46,628 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-88'
2025-05-22 00:08:46,628 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 46, 628282, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:46.628383] Packet received (Total: 89): b'TEST-88'
2025-05-22 00:08:51,629 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-89'
2025-05-22 00:08:51,629 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 51, 629654, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:51.629846] Packet received (Total: 90): b'TEST-89'
2025-05-22 00:08:56,630 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-90'
2025-05-22 00:08:56,630 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 8, 56, 630588, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:08:56.630687] Packet received (Total: 91): b'TEST-90'
2025-05-22 00:09:01,631 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-91'
2025-05-22 00:09:01,631 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 1, 631347, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:01.631458] Packet received (Total: 92): b'TEST-91'
2025-05-22 00:09:06,632 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-92'
2025-05-22 00:09:06,632 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 6, 632580, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:06.632762] Packet received (Total: 93): b'TEST-92'
2025-05-22 00:09:11,634 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-93'
2025-05-22 00:09:11,634 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 11, 634304, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:11.634407] Packet received (Total: 94): b'TEST-93'
2025-05-22 00:09:16,635 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-94'
2025-05-22 00:09:16,635 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 16, 635838, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:16.635936] Packet received (Total: 95): b'TEST-94'
2025-05-22 00:09:21,638 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-95'
2025-05-22 00:09:21,639 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 21, 639150, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:21.639368] Packet received (Total: 96): b'TEST-95'
2025-05-22 00:09:26,641 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-96'
2025-05-22 00:09:26,641 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 26, 641118, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:26.641215] Packet received (Total: 97): b'TEST-96'
2025-05-22 00:09:31,641 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-97'
2025-05-22 00:09:31,642 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 31, 642103, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:31.642221] Packet received (Total: 98): b'TEST-97'
2025-05-22 00:09:36,643 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-98'
2025-05-22 00:09:36,643 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 36, 643438, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:36.643625] Packet received (Total: 99): b'TEST-98'
2025-05-22 00:09:41,644 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 7 bytes
Sent packet: b'TEST-99'
2025-05-22 00:09:41,644 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 41, 644933, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:41.645046] Packet received (Total: 100): b'TEST-99'
2025-05-22 00:09:46,645 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-100'
2025-05-22 00:09:46,646 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 46, 646006, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:46.646123] Packet received (Total: 101): b'TEST-100'
2025-05-22 00:09:51,646 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-101'
2025-05-22 00:09:51,646 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 51, 646934, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:51.647040] Packet received (Total: 102): b'TEST-101'
2025-05-22 00:09:56,648 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-102'
2025-05-22 00:09:56,649 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 9, 56, 648999, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:09:56.649309] Packet received (Total: 103): b'TEST-102'
2025-05-22 00:10:01,650 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-103'
2025-05-22 00:10:01,650 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 1, 650509, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:01.650614] Packet received (Total: 104): b'TEST-103'
2025-05-22 00:10:06,651 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-104'
2025-05-22 00:10:06,651 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 6, 651890, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:06.651980] Packet received (Total: 105): b'TEST-104'
2025-05-22 00:10:11,653 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-105'
2025-05-22 00:10:11,653 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 11, 653874, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:11.654099] Packet received (Total: 106): b'TEST-105'
2025-05-22 00:10:16,655 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-106'
2025-05-22 00:10:16,655 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 16, 655772, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:16.655918] Packet received (Total: 107): b'TEST-106'
2025-05-22 00:10:21,657 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-107'
2025-05-22 00:10:21,657 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 21, 657641, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:21.657737] Packet received (Total: 108): b'TEST-107'
2025-05-22 00:10:26,659 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-108'
2025-05-22 00:10:26,659 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 26, 659756, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:26.660023] Packet received (Total: 109): b'TEST-108'
2025-05-22 00:10:31,661 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-109'
2025-05-22 00:10:31,662 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 31, 662016, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:31.662117] Packet received (Total: 110): b'TEST-109'
2025-05-22 00:10:36,662 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-110'
2025-05-22 00:10:36,663 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 36, 663083, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:36.663192] Packet received (Total: 111): b'TEST-110'
2025-05-22 00:10:41,663 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-111'
2025-05-22 00:10:41,663 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 41, 663763, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:41.663871] Packet received (Total: 112): b'TEST-111'
2025-05-22 00:10:46,665 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-112'
2025-05-22 00:10:46,665 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 46, 665287, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:46.665391] Packet received (Total: 113): b'TEST-112'
2025-05-22 00:10:51,666 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-113'
2025-05-22 00:10:51,666 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 51, 666574, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:51.666666] Packet received (Total: 114): b'TEST-113'
2025-05-22 00:10:56,668 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-114'
2025-05-22 00:10:56,668 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 10, 56, 668195, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:10:56.668329] Packet received (Total: 115): b'TEST-114'
2025-05-22 00:11:01,668 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-115'
2025-05-22 00:11:01,669 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 1, 669011, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:01.669110] Packet received (Total: 116): b'TEST-115'
2025-05-22 00:11:06,669 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-116'
2025-05-22 00:11:06,669 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 6, 669688, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:06.669787] Packet received (Total: 117): b'TEST-116'
2025-05-22 00:11:11,670 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-117'
2025-05-22 00:11:11,670 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 11, 670403, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:11.670514] Packet received (Total: 118): b'TEST-117'
2025-05-22 00:11:16,671 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-118'
2025-05-22 00:11:16,671 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 16, 671565, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:16.671768] Packet received (Total: 119): b'TEST-118'
2025-05-22 00:11:21,673 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-119'
2025-05-22 00:11:21,673 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 21, 673285, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:21.673417] Packet received (Total: 120): b'TEST-119'
2025-05-22 00:11:26,674 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-120'
2025-05-22 00:11:26,674 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 26, 674675, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:26.674787] Packet received (Total: 121): b'TEST-120'
2025-05-22 00:11:31,675 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-121'
2025-05-22 00:11:31,675 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 31, 675982, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:31.676181] Packet received (Total: 122): b'TEST-121'
2025-05-22 00:11:36,676 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-122'
2025-05-22 00:11:36,677 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 36, 677051, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:36.677163] Packet received (Total: 123): b'TEST-122'
2025-05-22 00:11:41,677 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-123'
2025-05-22 00:11:41,677 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 41, 677557, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:41.677739] Packet received (Total: 124): b'TEST-123'
2025-05-22 00:11:46,678 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-124'
2025-05-22 00:11:46,678 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 46, 678981, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:46.679219] Packet received (Total: 125): b'TEST-124'
2025-05-22 00:11:51,680 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-125'
2025-05-22 00:11:51,680 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 51, 680336, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:51.680443] Packet received (Total: 126): b'TEST-125'
2025-05-22 00:11:56,681 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-126'
2025-05-22 00:11:56,681 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 11, 56, 681610, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:11:56.681699] Packet received (Total: 127): b'TEST-126'
2025-05-22 00:12:01,682 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-127'
2025-05-22 00:12:01,682 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 1, 682654, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:01.682897] Packet received (Total: 128): b'TEST-127'
2025-05-22 00:12:06,683 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-128'
2025-05-22 00:12:06,684 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 6, 684066, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:06.684166] Packet received (Total: 129): b'TEST-128'
2025-05-22 00:12:11,685 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-129'
2025-05-22 00:12:11,685 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 11, 685342, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:11.685433] Packet received (Total: 130): b'TEST-129'
2025-05-22 00:12:16,686 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-130'
2025-05-22 00:12:16,686 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 16, 686418, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:16.686602] Packet received (Total: 131): b'TEST-130'
2025-05-22 00:12:21,687 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-131'
2025-05-22 00:12:21,687 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 21, 687808, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:21.687912] Packet received (Total: 132): b'TEST-131'
2025-05-22 00:12:26,688 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-132'
2025-05-22 00:12:26,688 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 26, 688332, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:26.688450] Packet received (Total: 133): b'TEST-132'
2025-05-22 00:12:31,689 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-133'
2025-05-22 00:12:31,689 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 31, 689688, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:31.689895] Packet received (Total: 134): b'TEST-133'
2025-05-22 00:12:36,691 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-134'
2025-05-22 00:12:36,691 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 36, 691163, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:36.691262] Packet received (Total: 135): b'TEST-134'
2025-05-22 00:12:41,692 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-135'
2025-05-22 00:12:41,692 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 41, 692238, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:41.692340] Packet received (Total: 136): b'TEST-135'
2025-05-22 00:12:46,692 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-136'
2025-05-22 00:12:46,693 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 46, 693217, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:46.693432] Packet received (Total: 137): b'TEST-136'
2025-05-22 00:12:51,693 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-137'
2025-05-22 00:12:51,693 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 51, 693884, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:51.693985] Packet received (Total: 138): b'TEST-137'
2025-05-22 00:12:56,695 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-138'
2025-05-22 00:12:56,695 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 12, 56, 695204, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:12:56.695303] Packet received (Total: 139): b'TEST-138'
2025-05-22 00:13:01,696 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-139'
2025-05-22 00:13:01,696 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 1, 696399, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:01.696606] Packet received (Total: 140): b'TEST-139'
2025-05-22 00:13:06,697 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-140'
2025-05-22 00:13:06,697 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 6, 697238, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:06.697365] Packet received (Total: 141): b'TEST-140'
2025-05-22 00:13:11,698 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-141'
2025-05-22 00:13:11,698 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 11, 698573, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:11.698675] Packet received (Total: 142): b'TEST-141'
2025-05-22 00:13:16,699 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-142'
2025-05-22 00:13:16,699 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 16, 699405, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:16.699503] Packet received (Total: 143): b'TEST-142'
2025-05-22 00:13:21,700 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-143'
2025-05-22 00:13:21,701 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 21, 701007, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:21.701179] Packet received (Total: 144): b'TEST-143'
2025-05-22 00:13:26,701 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-144'
2025-05-22 00:13:26,701 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 26, 701757, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:26.701849] Packet received (Total: 145): b'TEST-144'
2025-05-22 00:13:31,702 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-145'
2025-05-22 00:13:31,702 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 31, 702863, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:31.702954] Packet received (Total: 146): b'TEST-145'
2025-05-22 00:13:36,704 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-146'
2025-05-22 00:13:36,704 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 36, 704379, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:36.704509] Packet received (Total: 147): b'TEST-146'
2025-05-22 00:13:41,704 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-147'
2025-05-22 00:13:41,705 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 41, 704995, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:41.705110] Packet received (Total: 148): b'TEST-147'
2025-05-22 00:13:46,706 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-148'
2025-05-22 00:13:46,706 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 46, 706304, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:46.706402] Packet received (Total: 149): b'TEST-148'
2025-05-22 00:13:51,707 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-149'
2025-05-22 00:13:51,707 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 51, 707449, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:51.707679] Packet received (Total: 150): b'TEST-149'
2025-05-22 00:13:56,708 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-150'
2025-05-22 00:13:56,708 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 13, 56, 708670, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:13:56.708772] Packet received (Total: 151): b'TEST-150'
2025-05-22 00:14:01,709 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-151'
2025-05-22 00:14:01,709 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 1, 709948, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:01.710046] Packet received (Total: 152): b'TEST-151'
2025-05-22 00:14:06,710 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-152'
2025-05-22 00:14:06,710 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 6, 710590, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:06.710857] Packet received (Total: 153): b'TEST-152'
2025-05-22 00:14:11,711 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-153'
2025-05-22 00:14:11,711 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 11, 711984, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:11.712083] Packet received (Total: 154): b'TEST-153'
2025-05-22 00:14:16,712 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-154'
2025-05-22 00:14:16,712 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 16, 712625, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:16.712734] Packet received (Total: 155): b'TEST-154'
2025-05-22 00:14:21,713 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-155'
2025-05-22 00:14:21,713 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 21, 713454, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:21.713690] Packet received (Total: 156): b'TEST-155'
2025-05-22 00:14:26,714 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-156'
2025-05-22 00:14:26,714 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 26, 714347, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:26.714436] Packet received (Total: 157): b'TEST-156'
2025-05-22 00:14:31,714 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-157'
2025-05-22 00:14:31,714 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 31, 714749, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:31.714852] Packet received (Total: 158): b'TEST-157'
2025-05-22 00:14:36,715 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-158'
2025-05-22 00:14:36,715 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 36, 715726, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:36.715865] Packet received (Total: 159): b'TEST-158'
2025-05-22 00:14:41,716 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-159'
2025-05-22 00:14:41,716 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 41, 716469, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:41.716558] Packet received (Total: 160): b'TEST-159'
2025-05-22 00:14:46,717 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-160'
2025-05-22 00:14:46,717 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 46, 717525, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:46.717628] Packet received (Total: 161): b'TEST-160'
2025-05-22 00:14:51,718 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-161'
2025-05-22 00:14:51,718 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 51, 718932, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:51.719032] Packet received (Total: 162): b'TEST-161'
2025-05-22 00:14:56,720 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-162'
2025-05-22 00:14:56,720 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 14, 56, 720691, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:14:56.720798] Packet received (Total: 163): b'TEST-162'
2025-05-22 00:15:01,721 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-163'
2025-05-22 00:15:01,721 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 1, 721822, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:01.721926] Packet received (Total: 164): b'TEST-163'
2025-05-22 00:15:06,722 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-164'
2025-05-22 00:15:06,722 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 6, 722310, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:06.722416] Packet received (Total: 165): b'TEST-164'
2025-05-22 00:15:11,724 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-165'
2025-05-22 00:15:11,724 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 11, 724745, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:11.724902] Packet received (Total: 166): b'TEST-165'
2025-05-22 00:15:16,726 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-166'
2025-05-22 00:15:16,726 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 16, 726803, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:16.726943] Packet received (Total: 167): b'TEST-166'
2025-05-22 00:15:21,727 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-167'
2025-05-22 00:15:21,727 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 21, 727474, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:21.727588] Packet received (Total: 168): b'TEST-167'
2025-05-22 00:15:26,728 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-168'
2025-05-22 00:15:26,728 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 26, 728468, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:26.728577] Packet received (Total: 169): b'TEST-168'
2025-05-22 00:15:31,728 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-169'
2025-05-22 00:15:31,729 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 31, 729016, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:31.729117] Packet received (Total: 170): b'TEST-169'
2025-05-22 00:15:36,730 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-170'
2025-05-22 00:15:36,730 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 36, 730244, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:36.730346] Packet received (Total: 171): b'TEST-170'
2025-05-22 00:15:41,730 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-171'
2025-05-22 00:15:41,731 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 41, 731017, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:41.731140] Packet received (Total: 172): b'TEST-171'
2025-05-22 00:15:46,731 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-172'
2025-05-22 00:15:46,731 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 46, 731881, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:46.731975] Packet received (Total: 173): b'TEST-172'
2025-05-22 00:15:51,733 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-173'
2025-05-22 00:15:51,733 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 51, 733224, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:51.733332] Packet received (Total: 174): b'TEST-173'
2025-05-22 00:15:56,734 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-174'
2025-05-22 00:15:56,734 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 15, 56, 734314, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:15:56.734418] Packet received (Total: 175): b'TEST-174'
2025-05-22 00:16:01,735 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-175'
2025-05-22 00:16:01,735 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 1, 735737, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:01.735838] Packet received (Total: 176): b'TEST-175'
2025-05-22 00:16:06,737 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-176'
2025-05-22 00:16:06,737 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 6, 737695, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:06.737799] Packet received (Total: 177): b'TEST-176'
2025-05-22 00:16:11,738 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-177'
2025-05-22 00:16:11,738 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 11, 738325, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:11.738458] Packet received (Total: 178): b'TEST-177'
2025-05-22 00:16:16,739 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-178'
2025-05-22 00:16:16,739 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 16, 739503, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:16.739744] Packet received (Total: 179): b'TEST-178'
2025-05-22 00:16:21,740 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-179'
2025-05-22 00:16:21,740 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 21, 740553, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:21.740653] Packet received (Total: 180): b'TEST-179'
2025-05-22 00:16:26,741 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-180'
2025-05-22 00:16:26,741 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 26, 741586, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:26.741696] Packet received (Total: 181): b'TEST-180'
2025-05-22 00:16:31,742 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-181'
2025-05-22 00:16:31,742 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 31, 742555, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:31.742750] Packet received (Total: 182): b'TEST-181'
2025-05-22 00:16:36,743 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-182'
2025-05-22 00:16:36,743 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 36, 743640, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:36.743743] Packet received (Total: 183): b'TEST-182'
2025-05-22 00:16:41,745 - hardware.drivers.mock.rf - DEBUG - Queued packet for reception: 8 bytes
Sent packet: b'TEST-183'
2025-05-22 00:16:41,746 - hardware.drivers.mock.rf - DEBUG - Current signal metrics: SignalMetrics(rssi=-60.0, snr=25.0, frequency=433920000.0, channel=1, timestamp=datetime.datetime(2025, 5, 22, 4, 16, 41, 746061, tzinfo=datetime.timezone.utc))
Signal metrics: RSSI=-60.0 dBm, SNR=25.0 dB

[2025-05-22T00:16:41.746182] Packet received (Total: 184): b'TEST-183'
^C
Shutting down...
Cleaning up...
2025-05-22 00:16:42,365 - hardware.drivers.mock.rf - DEBUG - Receive loop cancelled
2025-05-22 00:16:42,365 - hardware.drivers.mock.rf - DEBUG - Stopped receiving packets
Done.

```
