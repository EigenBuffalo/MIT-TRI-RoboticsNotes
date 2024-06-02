FROM robotlocomotion/drake:jammy-20240412

RUN apt-get -q update && apt-get -q install -y --no-install-recommends nginx-light xvfb && apt-get -q clean

ENV DISPLAY=:1

ENV PATH="/opt/drake/bin:${PATH}" \
  PYTHONPATH="/opt/drake/lib/python3.10/site-packages:${PYTHONPATH}"