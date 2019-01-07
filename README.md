# Déploiement

En utilisant le bon préfixe IPv6, canal radio et PANID 802.15.4, déployer un
réseau RPL qui comprend :

- 1 noeud Border Router et
- 4 noeuds CoAP Erbium server.

```
user       canal  prefix                 IEEE802154_CONF_PANID
iotstras6  16     2001:660:4701:f0a5/64  0x0006
```

```
sudo tunslip6.py -v2 -L -a m3-$NODE_NUMBER -p 20000 2001:660:4701:f0a5::1/64
```

En s’inspirant du tutoriel suivant https://www.iot-lab.info/tutorials/contiki-coap-m3/ :

- [x] Configurer la couche MAC (NETSTACK_CONF_RDC) pour utiliser nullrdc_driver.
- [ ] Préciser les paramètres RPL utilisés : mode opératoire (storing ou non storing, type de trafic),
fonction objectif, métrique utilisée.
- [ ] Vérifier la connectivité IPv6 de vos noeuds (ping6, table de routage RPL BR, requêtes
CoAP vers les noeuds er-rest-example).
- [ ] Editer le code RPL de Contiki pour activer du debug sur le port série de chaque noeud afin
de pouvoir retracer les événements notables du protocole.
- [ ] Etablir un historique des événements RPL de chaque noeud et définir le temps de
convergence de RPL pour que tous les noeuds soient joignables.
- [x] Monitorer et sauvegarder la consommation énergétique de chacun des noeuds.
- [ ] Etudier les performances en terme de latence des messages, de paquets perdus : pendant 5
minutes, faites des requêtes GET vers chacun des 4 noeuds CoAP Erbium server avec un
intervalle de 5 secondes.
- [ ] Etudier les performances en terme de latence des messages, de paquets perdus : pendant 5
minutes, mettre les 4 noeuds CoAP Erbium serveur en mode Observe avec un intervalle de 5
secondes.

## RPL + CoAP + NullRDC

## RPL + CoAP + ContikiMAC

## RPL + CoAP + TSCH
