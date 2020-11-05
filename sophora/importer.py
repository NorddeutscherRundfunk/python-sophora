import logging.config
from bs4 import BeautifulSoup
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport


def import_xml(soap_config, xml):
    logger = logging.getLogger(__name__)
    try:
        session = Session()
        session.trust_env = False
        session.auth = HTTPBasicAuth(soap_config['user'], soap_config['password'])
        client = Client(soap_config['url'], transport=Transport(session=session))

        if soap_config['instance']:
            soap_result = client.service.importXmlToInstance(xml, soap_config['instance'])
        else:
            soap_result = client.service.importXml(xml)

        result_xml = BeautifulSoup(soap_result, 'xml')
        result = {
            'xml': result_xml
        }

        logger.info(str(result))
        if result_xml.importInformation['successful'] == "true":
            logger.info("Imported Sophora-XML for '%s' to '%s'", result_xml.sophoraId.text, soap_config['url'])
            result['successful'] = True
        else:
            logger.fatal("SOAP Import failed: %s", result_xml.importInformation.errorText.text)
            result['successful'] = False

        return result

    except Exception:
        logger.fatal("SOAP error: %s", soap_config['url'], exc_info=True)
