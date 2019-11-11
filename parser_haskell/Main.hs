import Data.Aeson
import qualified Data.ByteString.Lazy as B
import System.Exit

main = do
  stdin <- B.getContents
  exitWith $ case (decode stdin :: Maybe Value)
              of Nothing -> ExitFailure 1
                 Just _  -> ExitSuccess
