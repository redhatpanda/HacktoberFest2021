
/*Connections
    SD card Module - Arduino UNO
              MOSI - Pin 11
              MISO - Pin 12
              CLK  - Pin 13
              CS   - Pin 10
*/
#include <SPI.h>
#include <SD.h>

Sd2Card card;
SdVolume volume;
SdFile root;

const int chipSelect = 4;

void setup() 
{
  Serial.begin(9600);
  while (!Serial) 
  {
    ;
  }

  Serial.print("\nInitializing SD card...");

  if (!card.init(SPI_HALF_SPEED, chipSelect)) 
  {
    Serial.println("Initialization failed. Things to check:");
    Serial.println("* Is a card inserted?");
    Serial.println("* Is your wiring correct?");
    Serial.println("* Did you change the chipSelect pin to match your shield or module?");
    while (1);
  } 
  else 
  {
    Serial.println("A card is present and wiring is correct.");
  }

  Serial.println();
  Serial.print("Card type:         ");
  switch (card.type()) 
  {
    case SD_CARD_TYPE_SD1:
      Serial.println("SD1");
      break;
    case SD_CARD_TYPE_SD2:
      Serial.println("SD2");
      break;
    case SD_CARD_TYPE_SDHC:
      Serial.println("SDHC");
      break;
    default:
      Serial.println("Unknown");
  }

  if (!volume.init(card)) 
  {
    Serial.println("Could not find FAT16/FAT32 partition.\nMake sure you've formatted the card");
    while (1);
  }

  Serial.print("Clusters:          ");
  Serial.println(volume.clusterCount());
  Serial.print("Blocks x Cluster:  ");
  Serial.println(volume.blocksPerCluster());

  Serial.print("Total Blocks:      ");
  Serial.println(volume.blocksPerCluster() * volume.clusterCount());
  Serial.println();

  uint32_t volumesize;
  Serial.print("Volume type is:    FAT");
  Serial.println(volume.fatType(), DEC);

  volumesize = volume.blocksPerCluster();
  volumesize *= volume.clusterCount();
  volumesize /= 2;
  Serial.print("Volume size (Kb):  ");
  Serial.println(volumesize);
  Serial.print("Volume size (Mb):  ");
  volumesize /= 1024;
  Serial.println(volumesize);
  Serial.print("Volume size (Gb):  ");
  Serial.println((float)volumesize / 1024.0);

  Serial.println("\nFiles found on the card (name, date and size in bytes): ");
  root.openRoot(volume);

  // list all files in the card with date and size
  root.ls(LS_R | LS_DATE | LS_SIZE);
}

void loop(void) 
{
  
}
